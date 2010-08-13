test:
	./manage.py test -- --with-coverage --cover-package=tip -sd
clean:
	find . -name "*.pyc" -delete
