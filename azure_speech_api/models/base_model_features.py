# coding: utf-8

"""
    Speech Services API v3.1

    Speech Services API v3.1.  # noqa: E501

    OpenAPI spec version: v3.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from azure_speech_api.models.shared_model_features import SharedModelFeatures  # noqa: F401,E501

class BaseModelFeatures(SharedModelFeatures):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'supports_adaptations_with': 'list[DatasetKind]'
    }
    if hasattr(SharedModelFeatures, "swagger_types"):
        swagger_types.update(SharedModelFeatures.swagger_types)

    attribute_map = {
        'supports_adaptations_with': 'supportsAdaptationsWith'
    }
    if hasattr(SharedModelFeatures, "attribute_map"):
        attribute_map.update(SharedModelFeatures.attribute_map)

    def __init__(self, supports_adaptations_with=None, *args, **kwargs):  # noqa: E501
        """BaseModelFeatures - a model defined in Swagger"""  # noqa: E501
        self._supports_adaptations_with = None
        self.discriminator = None
        if supports_adaptations_with is not None:
            self.supports_adaptations_with = supports_adaptations_with
        SharedModelFeatures.__init__(self, *args, **kwargs)

    @property
    def supports_adaptations_with(self):
        """Gets the supports_adaptations_with of this BaseModelFeatures.  # noqa: E501

        Supported dataset kinds to adapt the model.  # noqa: E501

        :return: The supports_adaptations_with of this BaseModelFeatures.  # noqa: E501
        :rtype: list[DatasetKind]
        """
        return self._supports_adaptations_with

    @supports_adaptations_with.setter
    def supports_adaptations_with(self, supports_adaptations_with):
        """Sets the supports_adaptations_with of this BaseModelFeatures.

        Supported dataset kinds to adapt the model.  # noqa: E501

        :param supports_adaptations_with: The supports_adaptations_with of this BaseModelFeatures.  # noqa: E501
        :type: list[DatasetKind]
        """

        self._supports_adaptations_with = supports_adaptations_with

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(BaseModelFeatures, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BaseModelFeatures):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
