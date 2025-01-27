import heapq

def a_star(graph, start, goal, heuristic):
    """
    Algoritmo A* per trovare il percorso più breve in un grafo.

    Args:
        graph (dict): Rappresentazione del grafo come {nodo: [(vicino, costo)]}.
        start (any): Nodo di partenza.
        goal (any): Nodo obiettivo.
        heuristic (func): Funzione euristica h(n), stima del costo dal nodo n al goal.

    Returns:
        list: Percorso più breve dal nodo start al nodo goal, oppure [] se non esiste.
    """
    # Inizializza le strutture dati
    open_set = []  # Coda prioritaria
    heapq.heappush(open_set, (0, start))  # Inserisce (f_score, nodo)
    
    came_from = {}  # Tiene traccia del percorso
    g_score = {start: 0}  # Costo dal nodo di partenza
    f_score = {start: heuristic(start)}  # Stima totale (g + h)

    while open_set:
        # Prendi il nodo con il costo totale f_score più basso
        _, current = heapq.heappop(open_set)

        # Se abbiamo raggiunto il nodo obiettivo, ricostruisci il percorso
        if current == goal:
            return reconstruct_path(came_from, current)

        # Itera sui vicini del nodo corrente
        for neighbor, cost in graph.get(current, []):
            # Calcola il costo g provvisorio per raggiungere il vicino
            tentative_g_score = g_score[current] + cost

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                # Aggiorna i punteggi g e f
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor)

                # Se il vicino non è già nell'open_set, aggiungilo
                if all(neighbor != item[1] for item in open_set):
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    # Se l'open_set è vuoto e non abbiamo trovato il nodo obiettivo
    return []

def reconstruct_path(came_from, current):
    """
    Ricostruisce il percorso dal dizionario `came_from`.

    Args:
        came_from (dict): Dizionario con i predecessori di ogni nodo.
        current (any): Nodo obiettivo.

    Returns:
        list: Percorso dal nodo di partenza al nodo obiettivo.
    """
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.append(current)  # Aggiungi il nodo di partenza
    return path[::-1]  # Inverti il percorso