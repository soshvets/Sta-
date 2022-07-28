# stage1 as builder
FROM node:14.18.2 as builder

WORKDIR /app

# Copy the package.json and install dependencies
COPY frontend/package*.json ./
RUN npm install

# Copy rest of the files
# COPY . .

COPY /frontend/public/. ./public
COPY /frontend/src/. ./src
COPY /frontend/*.js ./

# Build the project
RUN npm run build

FROM nginx:stable

COPY --from=builder /app/dist /usr/share/nginx/html
# COPY ./frontend/nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./frontend/nginx/nginx.conf /etc/nginx/conf.d/default.conf

## Remove default nginx index page
# RUN rm -rf /usr/share/nginx/html/*

# Copy from the stahg 1

EXPOSE 80
ENTRYPOINT ["nginx", "-g", "daemon off;"]
