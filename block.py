import os

def block_websites(sites, redirect_ip="127.0.0.1"):
    """
    Блокирует доступ к указанным сайтам, добавляя их в файл hosts.
    
    :param sites: Список доменов для блокировки.
    :param redirect_ip: IP-адрес, на который будет перенаправлен трафик (по умолчанию 127.0.0.1).
    """
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts" if os.name == 'nt' else "/etc/hosts"
    try:
        # Чтение текущего содержимого файла hosts
        with open(hosts_path, 'r') as file:
            hosts_content = file.readlines()
        
        # Добавление новых записей
        with open(hosts_path, 'a') as file:
            for site in sites:
                entry = f"{redirect_ip} {site}\n"
                if entry not in hosts_content:
                    file.write(entry)
        
        print("Сайты успешно заблокированы. Перезагрузите браузер для применения.")
    
    except PermissionError:
        print("Ошибка: Для изменения файла hosts требуются права администратора.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Пример использования
websites_to_block = [
]

block_websites(websites_to_block)
