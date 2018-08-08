#! /bin/bash
wait_for_port() {
  local name="$1" host="$2" port="$3"
  local j=0
  while ! nc -z "$host" "$port" >/dev/null 2>&1 < /dev/null; do
    j=$((j+1))
    if [ $j -ge 20 ]; then
      echo >&2 "$(date) - $host:$port still not reachable, giving up"
      exit 1
    fi
    echo "$(date) - waiting for $name... $j/20"
    sleep 5
  done
}
wait_for_port mysql mysql 3306&&python manage.py migrate --settings=sc2w.conf.dev&&python manage.py runserver --settings=sc2w.conf.dev 0.0.0.0:8000