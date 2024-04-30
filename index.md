---
title: Stata keywords and packages
layout: withtable
---
Each entry in the database will list a **keyword** (something that Stata treats as a command or something similar), the **package** that contains it (with a link to search for the package on IDEAS), the **filename** where it is found, and the **extension** of the file.

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
    <td> <a href="https://ideas.repec.org/cgi-bin/htsearch?form=extended&wm=wrd&dt=range&ul=%25%2Fc%2F%25&q={{ row["package"] }}&cmd=Search!&wf=00F0&s=R" alt="Link to IDEAS" target="_blank">{{ row["package"] }}</a> </td>
    <td> {{ row["filename"] }} </td>
    <td> {{ row["extension"] }} </td>
  </tr>
  {% endfor %}
</table>



To download the entire database, [click here](https://raw.githubusercontent.com/social-science-data-editors/reference/main/_data/termsofuse.csv).