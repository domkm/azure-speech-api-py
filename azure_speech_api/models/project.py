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

class Project(object):
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
        'links': 'ProjectLinks',
        'properties': 'ProjectProperties',
        '_self': 'str',
        'display_name': 'str',
        'description': 'str',
        'locale': 'str',
        'custom_properties': 'dict(str, str)',
        'created_date_time': 'datetime'
    }

    attribute_map = {
        'links': 'links',
        'properties': 'properties',
        '_self': 'self',
        'display_name': 'displayName',
        'description': 'description',
        'locale': 'locale',
        'custom_properties': 'customProperties',
        'created_date_time': 'createdDateTime'
    }

    def __init__(self, links=None, properties=None, _self=None, display_name=None, description=None, locale=None, custom_properties=None, created_date_time=None):  # noqa: E501
        """Project - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._properties = None
        self.__self = None
        self._display_name = None
        self._description = None
        self._locale = None
        self._custom_properties = None
        self._created_date_time = None
        self.discriminator = None
        if links is not None:
            self.links = links
        if properties is not None:
            self.properties = properties
        if _self is not None:
            self._self = _self
        self.display_name = display_name
        if description is not None:
            self.description = description
        self.locale = locale
        if custom_properties is not None:
            self.custom_properties = custom_properties
        if created_date_time is not None:
            self.created_date_time = created_date_time

    @property
    def links(self):
        """Gets the links of this Project.  # noqa: E501


        :return: The links of this Project.  # noqa: E501
        :rtype: ProjectLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Project.


        :param links: The links of this Project.  # noqa: E501
        :type: ProjectLinks
        """

        self._links = links

    @property
    def properties(self):
        """Gets the properties of this Project.  # noqa: E501


        :return: The properties of this Project.  # noqa: E501
        :rtype: ProjectProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Project.


        :param properties: The properties of this Project.  # noqa: E501
        :type: ProjectProperties
        """

        self._properties = properties

    @property
    def _self(self):
        """Gets the _self of this Project.  # noqa: E501

        The location of this entity.  # noqa: E501

        :return: The _self of this Project.  # noqa: E501
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this Project.

        The location of this entity.  # noqa: E501

        :param _self: The _self of this Project.  # noqa: E501
        :type: str
        """

        self.__self = _self

    @property
    def display_name(self):
        """Gets the display_name of this Project.  # noqa: E501

        The display name of the object.  # noqa: E501

        :return: The display_name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Project.

        The display name of the object.  # noqa: E501

        :param display_name: The display_name of this Project.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this Project.  # noqa: E501

        The description of the object.  # noqa: E501

        :return: The description of this Project.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Project.

        The description of the object.  # noqa: E501

        :param description: The description of this Project.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def locale(self):
        """Gets the locale of this Project.  # noqa: E501

        The locale of the contained data.  # noqa: E501

        :return: The locale of this Project.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this Project.

        The locale of the contained data.  # noqa: E501

        :param locale: The locale of this Project.  # noqa: E501
        :type: str
        """
        if locale is None:
            raise ValueError("Invalid value for `locale`, must not be `None`")  # noqa: E501

        self._locale = locale

    @property
    def custom_properties(self):
        """Gets the custom_properties of this Project.  # noqa: E501

        The custom properties of this entity. The maximum allowed key length is 64 characters, the maximum  allowed value length is 256 characters and the count of allowed entries is 10.  # noqa: E501

        :return: The custom_properties of this Project.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this Project.

        The custom properties of this entity. The maximum allowed key length is 64 characters, the maximum  allowed value length is 256 characters and the count of allowed entries is 10.  # noqa: E501

        :param custom_properties: The custom_properties of this Project.  # noqa: E501
        :type: dict(str, str)
        """

        self._custom_properties = custom_properties

    @property
    def created_date_time(self):
        """Gets the created_date_time of this Project.  # noqa: E501

        The time-stamp when the object was created.  The time stamp is encoded as ISO 8601 date and time format  (\"YYYY-MM-DDThh:mm:ssZ\", see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations).  # noqa: E501

        :return: The created_date_time of this Project.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        """Sets the created_date_time of this Project.

        The time-stamp when the object was created.  The time stamp is encoded as ISO 8601 date and time format  (\"YYYY-MM-DDThh:mm:ssZ\", see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations).  # noqa: E501

        :param created_date_time: The created_date_time of this Project.  # noqa: E501
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
        if issubclass(Project, dict):
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
        if not isinstance(other, Project):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
