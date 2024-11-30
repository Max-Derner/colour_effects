# How to deploy new package version

## 1. Tag new version
* Update [`pyproject.toml`](./pyproject.toml) with new version
* Merge work to main branch
* Create [new release on GitHub](https://github.com/Max-Derner/colour_fx/releases/new)

## 2. Create new distribution
* Run `python3 -m build`
**N.B.** Never run build unless you are sure you have changed the version in `pyproject.toml`

## 3. Upload to [test PyPI](https://test.pypi.org/)
* `python3 -m twine upload --repository testpypi dist/*`

## 4. Test download
* `python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps colour_fx`

## 4. Upload to [PyPI](https://pypi.org)
* `twine upload dist/*`