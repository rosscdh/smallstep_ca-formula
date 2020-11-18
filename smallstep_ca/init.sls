{%- from "smallstep_ca/map.jinja" import config with context %}

smallstep_ca_python-pip:
  pkg.installed:
  - name: python-pip


smallstep_ca_install_compose:
  pip.installed:
  - name: docker-compose
  - require:
    - pkg: python-pip


{{ config.location }}:
  file.directory:
    - mode: 755
    - makedirs: True

{{ config.data_location }}:
  file.directory:
    - makedirs: True


{{ config.location }}/docker-compose.yml:
  file.managed:
  - source: salt://smallstep_ca/files/docker-compose.yml.jinja2
  - template: jinja

