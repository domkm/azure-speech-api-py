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

class ProjectLinks(object):
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
        'evaluations': 'str',
        'datasets': 'str',
        'models': 'str',
        'endpoints': 'str',
        'transcriptions': 'str'
    }

    attribute_map = {
        'evaluations': 'evaluations',
        'datasets': 'datasets',
        'models': 'models',
        'endpoints': 'endpoints',
        'transcriptions': 'transcriptions'
    }

    def __init__(self, evaluations=None, datasets=None, models=None, endpoints=None, transcriptions=None):  # noqa: E501
        """ProjectLinks - a model defined in Swagger"""  # noqa: E501
        self._evaluations = None
        self._datasets = None
        self._models = None
        self._endpoints = None
        self._transcriptions = None
        self.discriminator = None
        if evaluations is not None:
            self.evaluations = evaluations
        if datasets is not None:
            self.datasets = datasets
        if models is not None:
            self.models = models
        if endpoints is not None:
            self.endpoints = endpoints
        if transcriptions is not None:
            self.transcriptions = transcriptions

    @property
    def evaluations(self):
        """Gets the evaluations of this ProjectLinks.  # noqa: E501

        The location to get a list of all evaluations of this project. See operation \"Projects_ListEvaluations\" for more details.  # noqa: E501

        :return: The evaluations of this ProjectLinks.  # noqa: E501
        :rtype: str
        """
        return self._evaluations

    @evaluations.setter
    def evaluations(self, evaluations):
        """Sets the evaluations of this ProjectLinks.

        The location to get a list of all evaluations of this project. See operation \"Projects_ListEvaluations\" for more details.  # noqa: E501

        :param evaluations: The evaluations of this ProjectLinks.  # noqa: E501
        :type: str
        """

        self._evaluations = evaluations

    @property
    def datasets(self):
        """Gets the datasets of this ProjectLinks.  # noqa: E501

        The location to get a list of all datasets of this project. See operation \"Projects_ListDatasets\" for more details.  # noqa: E501

        :return: The datasets of this ProjectLinks.  # noqa: E501
        :rtype: str
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this ProjectLinks.

        The location to get a list of all datasets of this project. See operation \"Projects_ListDatasets\" for more details.  # noqa: E501

        :param datasets: The datasets of this ProjectLinks.  # noqa: E501
        :type: str
        """

        self._datasets = datasets

    @property
    def models(self):
        """Gets the models of this ProjectLinks.  # noqa: E501

        The location to get a list of all models of this project. See operation \"Projects_ListModels\" for more details.  # noqa: E501

        :return: The models of this ProjectLinks.  # noqa: E501
        :rtype: str
        """
        return self._models

    @models.setter
    def models(self, models):
        """Sets the models of this ProjectLinks.

        The location to get a list of all models of this project. See operation \"Projects_ListModels\" for more details.  # noqa: E501

        :param models: The models of this ProjectLinks.  # noqa: E501
        :type: str
        """

        self._models = models

    @property
    def endpoints(self):
        """Gets the endpoints of this ProjectLinks.  # noqa: E501

        The location to get a list of all endpoints of this project. See operation \"Projects_ListEndpoints\" for more details.  # noqa: E501

        :return: The endpoints of this ProjectLinks.  # noqa: E501
        :rtype: str
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this ProjectLinks.

        The location to get a list of all endpoints of this project. See operation \"Projects_ListEndpoints\" for more details.  # noqa: E501

        :param endpoints: The endpoints of this ProjectLinks.  # noqa: E501
        :type: str
        """

        self._endpoints = endpoints

    @property
    def transcriptions(self):
        """Gets the transcriptions of this ProjectLinks.  # noqa: E501

        The location to get a list of all transcriptions of this project. See operation \"Projects_ListTranscriptions\" for more details.  # noqa: E501

        :return: The transcriptions of this ProjectLinks.  # noqa: E501
        :rtype: str
        """
        return self._transcriptions

    @transcriptions.setter
    def transcriptions(self, transcriptions):
        """Sets the transcriptions of this ProjectLinks.

        The location to get a list of all transcriptions of this project. See operation \"Projects_ListTranscriptions\" for more details.  # noqa: E501

        :param transcriptions: The transcriptions of this ProjectLinks.  # noqa: E501
        :type: str
        """

        self._transcriptions = transcriptions

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
        if issubclass(ProjectLinks, dict):
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
        if not isinstance(other, ProjectLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
