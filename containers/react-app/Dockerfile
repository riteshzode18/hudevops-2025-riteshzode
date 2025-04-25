# Stage 1: Build the React app
FROM node:18-alpine AS builder

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the React app
RUN npm run build

# Stage 2: Serve the app with NGINX
FROM docker.io/library/nginx:1.27-alpine


# # Create a non-root user and group
# RUN addgroup -g 1001 appgroup && adduser -u 1001 -G appgroup -D appuser

# # Grant permissions to the non-root user for NGINX cache directories
# RUN mkdir -p /var/cache/nginx/client_temp && \
#     chown -R appuser:appgroup /var/cache/nginx /var/run /var/log/nginx

# # Switch to the non-root user
# USER appuser


# Copy custom NGINX configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy the React build files to NGINX's default directory
COPY --from=builder /app/build /usr/share/nginx/html

# Expose port 8080
EXPOSE 8080

# Start NGINX
CMD ["nginx", "-g", "daemon off;"]