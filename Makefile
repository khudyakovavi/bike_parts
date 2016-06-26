update:
	. ../env/bin/activate; \
	export DJANGO_SETTINGS_MODULE=bike_parts.settings.prod; \
	pip install -r requirements/prod.txt; \
	python manage.py collectstatic --no-input;
