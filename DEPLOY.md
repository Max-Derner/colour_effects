# How to deploy new package version

## 1. Tag new version
* Update [`pyproject.toml`](./pyproject.toml) with new version
* Commit work

## 2. Create new distribution
* Run `python -m build`
**N.B.** Never run build unless you are sure you have changed the version in `pyproject.toml`

## 3. Upload to [test PyPI](https://test.pypi.org/)
* `python -m twine upload --repository testpypi dist/colour_fx-<version>*`

## 4. Test download
* `pip install -i https://test.pypi.org/simple/ colour_fx`

## 5. Complete merge
* commit new distributions
* Tag version `git tag -a v<VERSION>`
* Merge work to main branch
* Create [new release on GitHub](https://github.com/Max-Derner/colour_fx/releases/new) with same version

## 6. Upload to [PyPI](https://pypi.org)
* `twine upload dist/colour_fx-<version>*`