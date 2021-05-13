import json, os

def setup():
    print('Welcome to the PyBuild project setup wizard. This wizard will help you set up the basic options in the pyconfig, but more can be added manually. ')
    print('You can press ^C at any time to quit the setup process.')

    project_name = input('Project name: ')
    ver = input('Project version: ')
    mainf = input('Main file: ')
    buildToExe = bool(input('Build to exe: '))
    publishToPyPi = bool(input('Publish package to PyPi: '))

    config = {
       "project": project_name,
       "version": ver,
       "main-file": mainf,
       "build-to-exe": buildToExe,
       "publish-to-pypi": publishToPyPi
    }

    config = json.dumps(config)

    os.mkdir('src')
    os.chdir('./src')

    with open('pyconfig.json', 'w') as f:
        f.write(str(config))
        f.close()