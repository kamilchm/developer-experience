.PHONY: clean dev lint docs

clean:
	rm -rf build dist

pex: dist/hn

dist/hn: wheel
	pex --cache-dir=dist -r hackernews_cli -e hncli.cli:cli -o dist/hn

wheel: lint
	python setup.py bdist_wheel

lint:
	prospector --zero-exit -s high hncli

dev:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
	pip install -r requirements-docs.txt
	python setup.py develop

docs:
	python setup.py build_sphinx

