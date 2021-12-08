"""
Author: Christian Oliveira
Created at: 2021-12-05
Description: Create app to simulation cloud environment.
Lenguage: Python
Version: 3.9.4
"""

from model.Server import Server
from utils.check_file import check_file, read_file
from utils.remove_special_caracters import remove_special_caracters


def write_report_output(servers_active, report):
    """
    Write in report about total cost of the servers.
    """
    if len(servers_active) > 0:
        quantity_servers = remove_special_caracters(str(servers_active))
        report.writelines(f"{quantity_servers}\n")
    else:
        report.writelines("0\n")

def create_server(ttask, umax, servers_active):
    # Create new instance servers.
    new_server = Server(ttask, umax)
    new_server.connect_user()
    servers_active.append(new_server)

def remove_servers(servers_active: list, remove_servers: list):
    # Remove servers empty.
    for server in remove_servers:
        server.setCostValue()
        servers_active.remove(server)


def add_tick_in_all_users(servers_active: list):
    list_remove = []
    for server in servers_active:
        server.check_tick_in_users()
        if server.getUsers() <= 0: 
            # Check servers is empty and add list remove.
            list_remove.append(server)
        else:
            # Add value R$ 1 for server to each tick.
            server.cost_value += 1

    remove_servers(servers_active, list_remove)


"""
Function main to the app.
"""
if __name__ == '__main__':
    if check_file():
        data_in_file = read_file()
        TTASK = data_in_file[0]
        UMAX = data_in_file[1]
        users = data_in_file[2:]

        if (1 <= TTASK <= 10) and (1 <= UMAX <= 10):
            report = open('temp/output.txt', 'w')
            servers_active = []

            for tick in range(10):
                try:
                    # interact users with each new tick.
                    quantity_users = users[tick]
                    for user in range(quantity_users):
                        if len(servers_active) > 0:
                            for server in servers_active[::-1]:
                                # Check if server has reached maximum limit.
                                if server.getUsers() < UMAX:
                                    server.connect_user()
                                else:
                                    create_server(TTASK, UMAX, servers_active)
                                break
                        else:
                            create_server(TTASK, UMAX, servers_active)
                except:
                    continue
                finally:
                    add_tick_in_all_users(servers_active)
                    write_report_output(servers_active, report)

            amount_to_pay = Server.total_cost()
            report.writelines(amount_to_pay)
            report.close()

        else:
            print(
                "400 - Dados de entrada para TTASK (1º linha) "+
                "e UMAX (2º linha) invalidos. "+
                "(min: 1 e max: 10 para ambos)"
            )
    else:
        print("404 - Arquivo não encontrado.")