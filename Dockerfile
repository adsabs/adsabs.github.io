FROM ruby:3.3-alpine

RUN apk add --no-cache \
    build-base \
    git \
    && gem install bundler

WORKDIR /site

COPY Gemfile Gemfile.lock ./
RUN bundle install --jobs 4

EXPOSE 4000

CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0"]
