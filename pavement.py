from paver.easy import *
from paver.setuputils import setup


setup(
    name ='behave-bdd',
    version ='0.1.0',
    description ="Behave Integration with Local Android, iOS and BrowserStack",
    license = "MIT",
    keywords = "python behave selenium appium android ios browserstack",
    packages=['features'],
    url='https://github.com/browserstack/lettuce-browserstack'
)

@task
def test():
    """Run all tests"""
    sh("paver run android")
    sh("paver run ios")
    sh("paver run browserstack")


@task
@consume_nargs(1)
def run(args):
    """Run test on android, ios and browserstack using different config."""
    if args[0] in ('android', 'ios', 'browserstack'):
        run_behave_test(args[0])
    else:
        print("""
        Only these commands are accepted
        ********************************
        paver run android
        paver run ios
        paver run browserstack
        ********************************
        """)


def run_behave_test(config, task_id=0):
    sh('CONFIG_FILE=config/{}.json TASK_ID={} behave'.format(config, task_id))
