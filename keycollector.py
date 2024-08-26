import os
import shutil

def copy_ssh_files(home_directory, destination_directory):
    """Copia archivos del directorio .ssh de cada usuario a un destino."""
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    
    for user_dir in os.listdir(home_directory):
        user_path = os.path.join(home_directory, user_dir)
        ssh_path = os.path.join(user_path, '.ssh')
        if os.path.isdir(user_path) and os.path.exists(ssh_path):
            dest_path = os.path.join(destination_directory, user_dir + '_ssh')
            shutil.copytree(ssh_path, dest_path)
            print(f"Archivos .ssh copiados desde {ssh_path} a {dest_path}")

def copy_postgres_config(destination_directory):
    """Copia archivos de configuración de PostgreSQL a un destino."""
    # Directorios comunes de configuración de PostgreSQL
    postgres_paths = ['/etc/postgresql', '/var/lib/pgsql']
    
    for path in postgres_paths:
        if os.path.exists(path):
            dest_path = os.path.join(destination_directory, os.path.basename(path))
            shutil.copytree(path, dest_path)
            print(f"Archivos de configuración de PostgreSQL copiados desde {path} a {dest_path}")

def main():
    home_directory = '/home'
    destination_directory = '/tmp/copied_files'  # Cambia esto al directorio donde deseas guardar los archivos

    # Copiar archivos .ssh
    copy_ssh_files(home_directory, destination_directory)

    # Copiar archivos de configuración de PostgreSQL
    copy_postgres_config(destination_directory)

if __name__ == "__main__":
    main()
