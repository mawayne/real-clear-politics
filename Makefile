
# Create a virtualenv and install requirements
install:
	virtualenv env
	env/bin/pip install -r requirements.txt
