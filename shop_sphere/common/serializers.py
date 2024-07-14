from rest_framework import serializers
from .utils import truncate


class TruncatedCharField(serializers.CharField):
    def to_internal_value(self, data):
        return truncate(data, self.max_length)

    def to_representation(self, data):
        return self.to_internal_value(data)
