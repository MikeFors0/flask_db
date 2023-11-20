gnome-terminal -e "bash -c \"source ./auth/bin/activate; exec bash\""
export FLASK_APP=project && \
export FLASK_ENV=development && \
flask run