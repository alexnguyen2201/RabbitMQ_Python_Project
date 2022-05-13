# The app was tested with Node v15.5.0
# So rather than using the 'latest' tag, it is safer to specify this particular version of node 
# for building the image. This can prevent compatibility issues with future releases of node.
FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Specify the working directory INSIDE the container
WORKDIR /usr/src/app

# Move the package.json and package-lock.json into the container to install dependencies
COPY Pipfile* ./

# Install the dependencies
RUN pip install pipenv

# use --system flag
# so it will install all packages into the system python
# and not into the virtualenv. Since docker containers do not need to have virtualenvs

# use --deploy flag, so your build will fail if your Pipfile.lock is out of date
# use --ignore-pipfile, so it won't mess with our setup
RUN pipenv install --system --deploy --ignore-pipfile

# Copy the source code
COPY . .

# Expose the port
EXPOSE 3000


# Start the node server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3000"]

