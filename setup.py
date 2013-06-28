from distutils.core import setup

setup(
    name='sentry-exception-type',
    version='1.0.0',
    url='https://github.com/zelo/sentry-exception-type',
    packages=['sentry_exception_type'],
    entry_points={
        'sentry.plugins': [
            'exception_type = sentry_exception_type.plugin:ExceptionTypePlugin'
        ],
    },
    zip_safe=False,
    include_package_data=True,
)