Backend based on Django-Rest framework
Front-end based on Vue

clean.json is a fixture, produced by parse.py, which processes the reddit data json lines.
Multiple KVPs are removed for brevity, and the output is formatted into a django compatible
fixture. This data was then loaded using "manage.py loaddata {{fixture}}".

Modules of the used venv are available in the requirements.txt. Note: not all of the modules
are actually used in the project, as I've reused the venv from other projects.