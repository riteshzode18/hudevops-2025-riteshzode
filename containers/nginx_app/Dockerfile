# Use the official Nginx image from Docker Hub
FROM docker.io/library/nginx:1.27-alpine

# Copy all files from the current directory to the Nginx web server directory
COPY . /usr/share/nginx/html

# Expose port 80 to the outside world
EXPOSE 80

# Start NGINX
CMD ["nginx", "-g", "daemon off;"]
