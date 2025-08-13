{{- define "news-app.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "news-app.fullname" -}}
{{- printf "%s" (include "news-app.name" .) -}}
{{- end -}}
