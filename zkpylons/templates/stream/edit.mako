<%inherit file="/base.mako" />

    <h2>Edit stream</h2>

    ${ h.form(h.url_for(id=c.stream.id)) }
<%include file="form.mako" />
      <p>${ h.submit('submit', 'Update') } ${ h.link_to('back', url=h.url_for(action='index', id=None)) }</p>
    ${ h.end_form() }
