---
name: archives
---
 
[return to overview](/interview)

# Archives

<ul>
  {% for post in site.posts reversed %}
    <li>
      <a href="{{ post.permalink }}">{{ post.title }}</a>
      <!-- <p>{{ post.excerpt | strip_html }}</p> -->
    </li>
  {% endfor %}
</ul>