PAGE_ACCESS_TOKEN="EAAUiQJbwNboBABscA7dPr6dtBll5yTwo4TZCybdV89aVBNXbAFMJFVKbcwcRef4WdIa261AYIakYYZArZAiXRsFcCCmqvDm9dVWh8e2ytgz1dC6BRwyXxAyOY8apXPNeTb7HhzoTjwAwxoxzfEs4nzr9HD2tTwtbZBxh0DveUQZDZD"
curl -X POST -H "Content-Type: application/json" -d '{
  "setting_type":"call_to_actions",
  "thread_state":"new_thread",
  "call_to_actions":[
    {
      "payload":"setup"
    }
  ]
}' "https://graph.facebook.com/v2.6/me/thread_settings?access_token=$PAGE_ACCESS_TOKEN"

curl -X POST -H "Content-Type: application/json" -d '{
  "persistent_menu":[
    {
      "locale":"default",
      "composer_input_disabled":false,
      "call_to_actions":[
        {
          "title":"Proximo jogo do meu time",
          "type":"postback",
          "payload":"proximo jogo"
        },
        {
          "type":"web_url",
          "title":"Globoesporte.com",
          "url":"http://globoesporte.globo.com",
          "webview_height_ratio":"full"
        }
      ]
    }
  ]
}' "https://graph.facebook.com/v2.6/me/messenger_profile?access_token=$PAGE_ACCESS_TOKEN"
