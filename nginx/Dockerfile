FROM nginx:1.19.0-alpine
COPY ./default.conf /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/nginx.conf
COPY get_docs.nginx.conf /etc/nginx/sites-available/get_docs.nginx.conf
RUN mkdir /etc/nginx/sites-enabled
RUN ln -s /etc/nginx/sites-available/get_docs.nginx.conf /etc/nginx/sites-enabled/
CMD ["nginx", "-g", "daemon off;"]
EXPOSE 80