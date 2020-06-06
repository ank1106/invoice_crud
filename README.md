# Invoice APP


## OS Dependencies

These instructions assume you're using Python 3 on a recent OS. Package names
may differ for Python 2 or for an older OS.

### Debian, Ubuntu, and friends

```
sudo apt install build-essential libpoppler-cpp-dev pkg-config python3-dev
```

### Fedora, Red Hat, and friends

```
sudo yum install gcc-c++ pkgconfig poppler-cpp-devel python3-devel
```

### macOS

```
brew install pkg-config poppler python
```

## Install requirements

```
pip install -r requirements.txt   
```

## Running test
```
python manage.py test   
```

## Initial user setup
```
python manage.py init_script   
```
above command creats two users client and staff. the staff user can be used to login to admin dashboard


## Docs

After installation of dependencies, migrations and initial user setup (python manage.py init_script)

### Swagger APIS
http://localhost:8000/swagger

### API docs
http://localhost:8000/docs

## [Video Walkthrough](https://drive.google.com/file/d/15FdzOgRDifPs-L3w4-_JmCx1JUFWoLj2/view?usp=sharing)




