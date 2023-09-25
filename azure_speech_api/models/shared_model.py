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

class SharedModel(object):
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
        '_self': 'str',
        'locale': 'str',
        'display_name': 'str',
        'description': 'str',
        'last_action_date_time': 'datetime',
        'status': 'Status',
        'created_date_time': 'datetime'
    }

    attribute_map = {
        '_self': 'self',
        'locale': 'locale',
        'display_name': 'displayName',
        'description': 'description',
        'last_action_date_time': 'lastActionDateTime',
        'status': 'status',
        'created_date_time': 'createdDateTime'
    }

    def __init__(self, _self=None, locale=None, display_name=None, description=None, last_action_date_time=None, status=None, created_date_time=None):  # noqa: E501
        """SharedModel - a model defined in Swagger"""  # noqa: E501
        self.__self = None
        self._locale = None
        self._display_name = None
        self._description = None
        self._last_action_date_time = None
        self._status = None
        self._created_date_time = None
        self.discriminator = None
        if _self is not None:
            self._self = _self
        self.locale = locale
        self.display_name = display_name
        if description is not None:
            self.description = description
        if last_action_date_time is not None:
            self.last_action_date_time = last_action_date_time
        if status is not None:
            self.status = status
        if created_date_time is not None:
            self.created_date_time = created_date_time

    @property
    def _self(self):
        """Gets the _self of this SharedModel.  # noqa: E501

        The location of this entity.  # noqa: E501

        :return: The _self of this SharedModel.  # noqa: E501
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this SharedModel.

        The location of this entity.  # noqa: E501

        :param _self: The _self of this SharedModel.  # noqa: E501
        :type: str
        """

        self.__self = _self

    @property
    def locale(self):
        """Gets the locale of this SharedModel.  # noqa: E501

        The locale of the contained data.  # noqa: E501

        :return: The locale of this SharedModel.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this SharedModel.

        The locale of the contained data.  # noqa: E501

        :param locale: The locale of this SharedModel.  # noqa: E501
        :type: str
        """
        if locale is None:
            raise ValueError("Invalid value for `locale`, must not be `None`")  # noqa: E501

        self._locale = locale

    @property
    def display_name(self):
        """Gets the display_name of this SharedModel.  # noqa: E501

        The display name of the object.  # noqa: E501

        :return: The display_name of this SharedModel.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this SharedModel.

        The display name of the object.  # noqa: E501

        :param display_name: The display_name of this SharedModel.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this SharedModel.  # noqa: E501

        The description of the object.  # noqa: E501

        :return: The description of this SharedModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SharedModel.

        The description of the object.  # noqa: E501

        :param description: The description of this SharedModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def last_action_date_time(self):
        """Gets the last_action_date_time of this SharedModel.  # noqa: E501

        The time-stamp when the current status was entered.  The time stamp is encoded as ISO 8601 date and time format  (\"YYYY-MM-DDThh:mm:ssZ\", see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations).  # noqa: E501

        :return: The last_action_date_time of this SharedModel.  # noqa: E501
        :rtype: datetime
        """
        return self._last_action_date_time

    @last_action_date_time.setter
    def last_action_date_time(self, last_action_date_time):
        """Sets the last_action_date_time of this SharedModel.

        The time-stamp when the current status was entered.  The time stamp is encoded as ISO 8601 date and time format  (\"YYYY-MM-DDThh:mm:ssZ\", see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations).  # noqa: E501

        :param last_action_date_time: The last_action_date_time of this SharedModel.  # noqa: E501
        :type: datetime
        """

        self._last_action_date_time = last_action_date_time

    @property
    def status(self):
        """Gets the status of this SharedModel.  # noqa: E501


        :return: The status of this SharedModel.  # noqa: E501
        :rtype: Status
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SharedModel.


        :param status: The status of this SharedModel.  # noqa: E501
        :type: Status
        """

        self._status = status

    @property
    def created_date_time(self):
        """Gets the created_date_time of this SharedModel.  # noqa: E501

        The time-stamp when the object was created.  The time stamp is encoded as ISO 8601 date and time format  (\"YYYY-MM-DDThh:mm:ssZ\", see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations).  # noqa: E501

        :return: The created_date_time of this SharedModel.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        """Sets the created_date_time of this SharedModel.

        The time-stamp when the object was created.  The time stamp is encoded as ISO 8601 date and time format  (\"YYYY-MM-DDThh:mm:ssZ\", see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations).  # noqa: E501

        :param created_date_time: The created_date_time of this SharedModel.  # noqa: E501
        :type: datetime
        """

        self._created_date_time = created_date_time

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
        if issubclass(SharedModel, dict):
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
        if not isinstance(other, SharedModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
