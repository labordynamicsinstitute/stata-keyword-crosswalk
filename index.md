---
title: Stata keywords and packages
layout: withtable
---
Each entry in the database will list a data provider, an extract from the terms of use, and the source URL for the terms of use. There is an indication on whether extracts from the data provider can be redistributed by academics as part of replication packages (an important caveat!). When available, there may be separate page with further details.

> Search the database for any keyword in any field.


<table class="display">
  {% for row in site.data.keyword-package-crosswalk %}
    {% if forloop.first %}
    <thead>
    <tr>
      {% for cell in row %}
        <th>{{ cell[0] }}</th>
        {% endif %}
      {% endfor %}
    </tr>
    </thead>
    {% endif %}

  <!-- manually constructing table -->
  <!-- keyword,package,filename,extension -->
  <tr>
    <td> {{ row["keyword"] }} </td>
    <td> {{ row["package"] }} </td>
    <td> {{ row["filename"] }} </td>
    <td> {{ row["extension"] }} </td>
  </tr>
  {% endfor %}
</table>



To download the entire database, [click here](https://raw.githubusercontent.com/social-science-data-editors/reference/main/_data/termsofuse.csv).