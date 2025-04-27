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

# Create a non-root user and group
RUN addgroup -g 1001 appgroup && adduser -u 1001 -G appgroup -D appuser

# Copy React build files with ownership set to the non-root user
COPY --chown=appuser:appgroup --from=builder /app/build /usr/share/nginx/html

# Grant permissions to the non-root user for NGINX directories
RUN chmod -R 755 /usr/share/nginx/html && \
    mkdir -p /var/cache/nginx/client_temp /run && \
    chown -R appuser:appgroup /var/cache/nginx /var/run /var/log/nginx /run

# Switch to the non-root user
USER appuser

# Copy custom NGINX configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 8080
EXPOSE 8080

# Start NGINX
CMD ["nginx", "-g", "daemon off;"]

# bug was non-root user not having permission to access run directory and /usr/share/nginx/html