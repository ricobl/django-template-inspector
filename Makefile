test: clean
	@python manage.py test -- --verbose --with-coverage --cover-package=tip -sd
clean:
	@find . -name "*.pyc" -delete
install:
	@python setup.py install
	@rm -rf build/ dist/ *.egg-info
uninstall:
	@pip uninstall django-tip
