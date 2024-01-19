from django_intro_app.models import Train, TrainRegistration


class TrainRepository:
    def get_by_id(self, train_id: str) -> Train:
        return Train.objects.get(id=train_id)

    def find_registration_by_train(self, train: Train) -> TrainRegistration:
        return TrainRegistration.objects \
            .select_related('tracking_device') \
            .filter(train=train)

    def create_registration(self, train_registration: TrainRegistration):
        train_registration.save()