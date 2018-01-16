[return to overview](overview)

# Archives

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.permalink }}">{{ post.title }}</a>
      <p>{{ page.excerpt | strip_html }}</p>
    </li>
  {% endfor %}
</ul>
