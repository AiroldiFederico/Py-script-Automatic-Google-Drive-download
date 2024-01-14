# Google Drive Folder Downloader

## Descrizione
Questo script Python è progettato per scaricare tutti i file presenti in una specifica cartella di Google Drive su una cartella locale del tuo computer. È utile per automatizzare il processo di download di file da Google Drive senza doverli scaricare manualmente uno per uno.

## Caratteristiche
- Scarica tutti i file da una specifica cartella di Google Drive.
- Ignora le sottocartelle per una gestione più semplice e diretta.
- Utilizza l'API di Google Drive per l'accesso e il download dei file.

## Come Funziona
Lo script si collega a Google Drive tramite l'API di Google, cerca tutti i file presenti in una cartella specificata dall'utente, e li scarica in una cartella locale sul computer dell'utente.

## Prerequisiti
- Python 3
- Accesso a Internet
- Account Google

## Installazione delle Librerie
Esegui il seguente comando per installare le librerie Python necessarie:

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

## Configurazione dell'Ambiente Virtuale

L'uso di un ambiente virtuale è consigliato per gestire le dipendenze del progetto. Ecco come configurarlo:

### Creazione dell'Ambiente Virtuale
- Apri il terminale e naviga alla directory del progetto.
- Esegui il seguente comando per creare un ambiente virtuale:
  ```bash
  python -m venv myenv
  ```
  Sostituisci `myenv` con il nome che desideri dare al tuo ambiente virtuale.

### Attivazione dell'Ambiente Virtuale
- Attiva l'ambiente virtuale con il comando:
  - Su Windows:
    ```bash
    myenv\Scripts\activate
    ```
  - Su macOS/Linux:
    ```bash
    source myenv/bin/activate
    ```

### Installazione delle Dipendenze nell'Ambiente Virtuale
- Con l'ambiente virtuale attivo, installa le librerie richieste:
  ```bash
  pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
  ```

### Disattivazione dell'Ambiente Virtuale
- Quando hai finito di lavorare nel progetto, puoi disattivare l'ambiente virtuale con:
  ```bash
  deactivate
  ```

## Comandi per Eseguire lo Script

Assicurati che l'ambiente virtuale sia attivo e che tutte le dipendenze siano state installate. Poi segui questi passaggi:

1. **Esegui lo Script**:
   ```bash
   python nome_script.py
   ```
   Sostituisci `nome_script.py` con il nome effettivo del tuo file Python.

2. **Inserisci l'URL della Cartella di Google Drive** quando richiesto dallo script.

3. **Inserisci il Percorso della Cartella Locale** dove desideri salvare i file scaricati.

4. **Completa il Processo di Autenticazione** nel browser che si apre.


---

Ora passerò alla seconda parte, che includerà i dettagli su come ottenere il `credentials.json` e altre informazioni.

---

## Ottenimento del File `credentials.json`

Per utilizzare lo script, hai bisogno di un file `credentials.json`, che permette l'autenticazione con l'API di Google Drive. Ecco come ottenerlo:

### 1. Configura Google Cloud Platform
- Vai su [Google Cloud Console](https://console.cloud.google.com/).
- Crea un nuovo progetto o seleziona un progetto esistente.
- Naviga in "API & Services" > "Dashboard" e abilita l'API di Google Drive per il tuo progetto.

### 2. Crea le Credenziali OAuth
- Nella Google Cloud Console, vai alla pagina "Credentials".
- Clicca su "Create Credentials" e seleziona "OAuth client ID".
- Configura lo schermo di consenso OAuth fornendo le informazioni richieste.
- Sotto "Application type", scegli "Desktop app" e dai un nome alla tua credenziale.
- Scarica il file `credentials.json` dopo aver creato le credenziali.

## Uso dello Script
- Posiziona il file `credentials.json` nella stessa directory dello script.
- Esegui lo script Python. Ti verrà chiesto di inserire l'URL della cartella Google Drive e il percorso della cartella locale dove desideri salvare i file.
- Segui la procedura di autenticazione nel browser che si apre automaticamente.

## Autore
Federico Airoldi, BG Italy 

## Data e Versione
 Versione 1.0  -> 3 Gennaio 2024

