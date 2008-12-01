<h2>List of Registration Notes</h2>

<table>
    <tr>
        <th>ID/Edit</th>
        <th>For person</th>
        <th>Note</th>
        <th>Written By</th>
        <th>Created</th>
        <th>Last updated</th>
        <th>Delete</th>
    </tr>

% for d in c.rego_note_collection:
%   print d
    <tr class="<% h.cycle('even', 'odd')%>">
        <td><% h.link_to(str(d.id) + ' (edit)', url=h.url(controller='rego_note', action='edit', id=d.id)) %></td>
        <td><% h.link_to(d.rego.person.firstname + ' ' + d.rego.person.lastname, h.url(controller='person', action='view', id=d.rego.person.id)) %>, <% h.link_to('View Registration', h.url(controller='registration', action='view', id=d.rego.id)) %></td>
        <td><% h.line_break(d.note) %>
        <td><% h.link_to(d.by.firstname + ' ' + d.by.lastname, h.url(controller='person', action='view', id=d.by.id)) %></td>
        <td><% d.creation_timestamp.strftime("%Y-%m-%d&nbsp;%H:%M") %></td>
        <td><% d.last_modification_timestamp.strftime("%Y-%m-%d&nbsp;%H:%M") %></td>
        <td><% h.link_to('X (delete)', url=h.url(controller='rego_note', action='delete', id=d.id)) %></td>
    </tr>
% #endfor
</table>
<p><% h.link_to('Add another', url=h.url(controller='rego_note', action='new')) %></p>

<%method title>
List of DB pages - <& PARENT:title &>
</%method>

<%init>
</%init>