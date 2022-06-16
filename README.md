# tackle-integration-tests

$ python3.9 -m venv ./venv/ # Create the Virtual Enviroment.

$ source venv/bin/activate # Activate the Virtual Enviroment Just Created.

From inside the virtual env:

$ pip install -r requirements.txt

## Run Tests

From inside the virtual env:
$ export TACKLE_USER=<user> && export TACKLE_USER=<user> $$ export TACKLE_PASSWORD=<pass> && export TACKLE_URL=<url> (including http:// Or https:// and without no closing /)
 
$ python3.9  -m pytest /home/amos/git/tackle-integration-tests/tests/test_tags.py


### Just Get token

$ python3.9 get-token.py --user=admin --password=XXXX --host <tackle-url> (including http:// Or https:// and without no closing /)

