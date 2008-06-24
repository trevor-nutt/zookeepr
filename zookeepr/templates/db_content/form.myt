<fieldset>

<p class="label">
<span class="mandatory">*</span>
<label for="db_content.title">Title:</label>
</p><p class="entries">
<% h.textfield('db_content.title', size=60) %>
</p>

<p class="label"><span class="mandatory">*</span><span class="publishable">&#8224;</span><label>Content Type:</label></p>
<p class="entries">
% for st in c.db_content_types:
<label><% h.radio('db_content.type', st.id) %> <% st.name |h %></label><br>
% #endfor
</p>

<p class="label">
<label for="db_content.url">URL:</label>
</p><p class="entries">
<% h.textfield('db_content.url', size=60) %>
</p>
<ul class="note"><li>For pages and news items the URL after the linux.conf.au/ that this page should be rendered for. EG: 'about/linux'.<br>
You don't have to supply a URL as content is still accessible via ID's. It is recommended not to create a URL alias for news items.</li>
<li>For "In the press" this is the URL you want the item to.</li></ul>

<p class="label">
<label for="db_content.body">Body:</label>
</p><p class="entries">
<% h.textarea('db_content.body', size="70x6") %>
</p>
<ul class="note"><li>The HTML rendered body. Please surround by &lt;p&gt; tags when appropriate. Use &lt;h3&gt;'s to automatically create a "contents" section.</li>
<li>For news articles you can place a &lt;!--break--&gt; statement to separate the entire body from the preview on the news page.</li>
<li>For in the press this becomes the comment next to the link.</li></ul>
<p>
<% h.submitbutton('Save') %>
</p>
</fieldset>

