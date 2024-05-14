import csv

from django.core.management.base import BaseCommand, CommandError
from courses_api.models import Provider, Course
import pathlib


class Command(BaseCommand):
    help = "Import data from a file"

    def add_arguments(self, parser):
        parser.add_argument("filename", nargs="+", type=str)

    def handle(self, *args, **options):
        for filename in options["filename"]:
            try:
                file = pathlib.Path(__file__).joinpath(f'../../../../{filename}').resolve()
                with open(file) as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if row[0] != 'id':
                            if filename == 'providers.csv':
                                for item in range(5 - row.__len__()):
                                    row.append(None)
                                _, created = Provider.objects.get_or_create(
                                    id=row[0],
                                    description=row[1],
                                    name=row[2],
                                    url=row[3],
                                    image=row[4],
                                )
                            elif filename == 'courses.csv':
                                for item in range(5 - row.__len__()):
                                    row.append("")
                                _, created = Course.objects.get_or_create(
                                    id=row[0],
                                    description=row[1],
                                    title=row[2],
                                    provider=Provider.objects.get(id=row[3]),
                                    price=row[4],
                                )
            except Provider.DoesNotExist:
                raise CommandError('File "%s" does not exist' % filename)
            self.stdout.write(
                self.style.SUCCESS('Successfully imported data from "%s"' % filename)
            )
