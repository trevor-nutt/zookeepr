"""The application's model objects"""
import sqlalchemy as sa

from meta import Base
from pylons.controllers.util import abort
from zookeepr.model.meta import Session
from zookeepr.lib.model import CommaList

from person import Person
from funding_attachment import FundingAttachment

def setup(meta):
   meta.Session.add_all(
        [
            FundingStatus(name='Accepted'),
            FundingStatus(name='Declined'),
            FundingStatus(name='Pending'),
            FundingStatus(name='Withdrawn'),
        ]
   )
   meta.Session.add_all(
        [
            FundingType(name='InternetNZ Oceania Programme', active=True),
            FundingType(name='InternetNZ Kiwi Programme', active=True),
            FundingType(name='Google Diversity Programme', active=True),
        ]
    )


class FundingStatus(Base):
    """Stores funding status
    """
    __tablename__ = 'funding_status'

    id = sa.Column(sa.types.Integer, primary_key=True)

    # name of status
    name = sa.Column(sa.types.String(40), unique=True, nullable=False)

    def __init__(self, **kwargs):
        # remove the args that should never be set via creation
        super(FundingStatus, self).__init__(**kwargs)

    @classmethod
    def find_by_id(cls, id):
        return Session.query(FundingStatus).filter_by(id=id).first()

    @classmethod
    def find_by_name(cls, name):
        return Session.query(FundingStatus).filter_by(name=name).first()

    @classmethod
    def find_all(cls):
        return Session.query(FundingStatus).order_by(FundingStatus.name).all()

class FundingType(Base):
    """Stores funding types
    """
    __tablename__ = 'funding_type'

    id = sa.Column(sa.types.Integer, primary_key=True)
    active = sa.Column(sa.types.Boolean, nullable=False)

    # title of type
    name = sa.Column(sa.types.String(40), unique=True, nullable=False)

    def __init__(self, **kwargs):
        # remove the args that should never be set via creation
        super(FundingType, self).__init__(**kwargs)

    @classmethod
    def find_by_id(cls, id):
        return Session.query(FundingType).filter_by(id=id).first()

    @classmethod
    def find_by_name(cls, name):
        return Session.query(FundingType).filter_by(name=name).first()

    @classmethod
    def find_all(cls):
        return Session.query(FundingType).order_by(FundingType.name).all()


class Funding(Base):
    __tablename__ = 'funding'

    id = sa.Column('id', sa.types.Integer, primary_key=True)
    person_id = sa.Column(sa.types.Integer, sa.ForeignKey('person.id'))
    status_id = sa.Column(sa.types.Integer, sa.ForeignKey('funding_status.id'))
    funding_type_id = sa.Column(sa.types.Integer, sa.ForeignKey('funding_type.id'))

    male = sa.Column(sa.types.Boolean)
    why_attend = sa.Column(sa.types.Text)
    how_contribute = sa.Column(sa.types.Text)
    financial_circumstances = sa.Column(sa.types.Text)
    diverse_groups = sa.Column(sa.types.Text)
    supporting_information = sa.Column(sa.types.Text)
    prevlca = sa.Column(CommaList)

    creation_timestamp = sa.Column(sa.types.DateTime, nullable=False,
                                       default=sa.func.current_timestamp())
    last_modification_timestamp = sa.Column(sa.types.DateTime,
        nullable=False, default=sa.func.current_timestamp(),
        onupdate=sa.func.current_timestamp())

    #person = sa.orm.relation(Person, backref='funding', cascade="all, delete-orphan", lazy=True, uselist=False, single_parent=True)
    person = sa.orm.relation(Person, backref='funding', lazy=True, uselist=False)
    type = sa.orm.relation(FundingType)
    status = sa.orm.relation(FundingStatus)
    attachments = sa.orm.relation(FundingAttachment, lazy=True, cascade='all, delete-orphan')

    # Only allow one application per person per funding type.
    sa.UniqueConstraint(person_id, funding_type_id, name='person_funding_type')


    def __init__(self, **kwargs):
        super(Funding, self).__init__(**kwargs)

    def available(self):
        if self.active:
           return True
        else:
           return False

    def __repr__(self):
        return '<Funding id=%r person_id=%r>' % (self.id, self.person_id)

    @classmethod
    def find_by_id(cls, id, abort_404 = True):
        result = Session.query(Funding).filter_by(id=id).first()
        if result is None and abort_404:
            abort(404, "No such Funding object")
        return result
        
    @classmethod
    def find_all(cls):
        return Session.query(Funding).order_by(Funding.id).all()
