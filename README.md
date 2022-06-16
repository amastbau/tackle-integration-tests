# tackle-integration-tests

$ python3.9 -m venv ./venv/ # Create the Virtual Enviroment.

$ source venv/bin/activate # Activate the Virtual Enviroment Just Created.

From inside the virtual env:

$ pip install -r requirements.txt

## Run Tests

### Using podman docker

$ podman rmi tackle-integration-tests # If needed
$ podman build -f Dockerfile -t tackle-integration-tests &&
  podman run -e TACKLE_USER='' -e TACKLE_PASSWORD='' -e TACKLE_URL='http://' tackle-integration-tests



### From inside the virtual env:

$ export TACKLE_USER=<user> && export TACKLE_USER=<user> && export TACKLE_PASSWORD=<pass> && export TACKLE_URL=<url> (including http:// Or https:// and without no closing /)
 
$ python3.9  -m pytest /home/amos/git/tackle-integration-tests/tests/test_tags.py


### Just Get token

$ python3.9 get-token.py --user=admin --password=XXXX --host <tackle-url> (including http:// Or https:// and without no closing /)
 
### How to Contribute
TBD
at this point, simply branch and send PRs
the is a tox file, so you can try running tox, it might have not been tested yet.

