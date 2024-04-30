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
      {% endfor %}
    </tr>
    </thead>
    {% endif %}

  <!-- manually constructing table -->
  <!-- keyword,package,filename,extension -->
  <tr>
    <td> {{ row["keyword"] }} </td>
    <td> <a href="https://ideas.repec.org/cgi-bin/htsearch?form=extended&wm=wrd&dt=range&ul=%25%2Fc%2F%25&q={{ row["package"] }}&cmd=Search!&wf=00F0&s=R" alt="Link to IDEAS">{{ row["package"] }}</a> </td>
    <td> {{ row["filename"] }} </td>
    <td> {{ row["extension"] }} </td>
  </tr>
  {% endfor %}
</table>



To download the entire database, [click here](https://raw.githubusercontent.com/social-science-data-editors/reference/main/_data/termsofuse.csv).