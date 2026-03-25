# Philos - Frases Filos\u00f3ficas

App de frases filos\u00f3ficas com 160+ cita\u00e7\u00f5es de grandes pensadores, organizadas por escola, autor e sentimento. Dispon\u00edvel em portugu\u00eas, ingl\u00eas e espanhol.

## Getting Started

```bash
flutter pub get
flutter run
```

## Configura\u00e7\u00e3o do Widget iOS (WidgetKit)

O arquivo Swift j\u00e1 est\u00e1 pronto em `ios/PhilosWidget/PhilosWidget.swift`. Para que o widget funcione no iOS, siga os passos abaixo no Xcode:

### 1. Abrir o projeto no Xcode

```bash
open ios/Runner.xcworkspace
```

### 2. Adicionar o Widget Extension target

1. No Xcode, v\u00e1 em **File \u2192 New \u2192 Target...**
2. Selecione **Widget Extension**
3. Nomeie como `PhilosWidget`
4. **Desmarque** "Include Configuration App Intent"
5. **Desmarque** "Include Live Activity"
6. Clique em **Finish**
7. Se o Xcode perguntar "Activate scheme?", clique em **Activate**

### 3. Substituir o c\u00f3digo gerado

O Xcode vai criar alguns arquivos automaticamente. Substitua todo o conte\u00fado do arquivo Swift gerado pelo conte\u00fado de `ios/PhilosWidget/PhilosWidget.swift` (que j\u00e1 est\u00e1 pronto no reposit\u00f3rio).

### 4. Configurar App Groups

O App Group permite que o app principal e o widget compartilhem dados (a frase atual).

**No target `Runner` (app principal):**
1. Selecione o target **Runner** na barra lateral
2. V\u00e1 na aba **Signing & Capabilities**
3. Clique em **+ Capability**
4. Procure e adicione **App Groups**
5. Adicione o grupo: `group.com.gambitstudio.philos`

**No target `PhilosWidgetExtension`:**
1. Selecione o target **PhilosWidgetExtension** na barra lateral
2. V\u00e1 na aba **Signing & Capabilities**
3. Clique em **+ Capability**
4. Procure e adicione **App Groups**
5. Adicione o **mesmo** grupo: `group.com.gambitstudio.philos`

### 5. Configurar o Bundle Identifier

1. No target **PhilosWidgetExtension**, v\u00e1 em **General**
2. Defina o Bundle Identifier como: `com.gambitstudio.philos.PhilosWidget`
3. Selecione o **Team** de assinatura correto (o mesmo do Runner)

### 6. Configurar o Deployment Target

1. No target **PhilosWidgetExtension**, v\u00e1 em **General**
2. Defina o **Minimum Deployments** como **iOS 17.0** (ou o mesmo do Runner)

### 7. Build e testar

```bash
flutter build ios
```

Ou no Xcode, selecione o scheme **Runner** e fa\u00e7a o build normalmente. O widget ser\u00e1 inclu\u00eddo automaticamente.

### Verificar se est\u00e1 funcionando

1. Instale o app no dispositivo/simulador
2. V\u00e1 para a tela inicial do iPhone
3. Segure pressionado em uma \u00e1rea vazia
4. Toque no **"+"** no canto superior
5. Procure por **"Philos"**
6. Adicione o widget

### Troubleshooting

- **Widget n\u00e3o aparece na lista:** Certifique-se de que o target `PhilosWidgetExtension` est\u00e1 sendo compilado junto com o Runner. Verifique em **Runner \u2192 Build Phases \u2192 Embed App Extensions**.
- **Widget mostra "Toque para abrir o Philos":** Abra o app pelo menos uma vez para que ele salve a frase no App Group compartilhado.
- **Erro de App Group:** Verifique se o identificador `group.com.gambitstudio.philos` est\u00e1 id\u00eantico nos dois targets (Runner e PhilosWidgetExtension). Qualquer diferen\u00e7a de caractere faz falhar.
- **Erro de assinatura:** Ambos os targets precisam usar o mesmo Team e o App Group precisa estar registrado no Apple Developer Portal.

## Widget Android

O widget Android j\u00e1 funciona automaticamente. O `QuoteWidgetProvider` est\u00e1 configurado em `android/app/src/main/kotlin/` e o layout em `android/app/src/main/res/layout/quote_widget.xml`.
