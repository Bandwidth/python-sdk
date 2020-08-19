"""
bridge.py

Representation of Bandwidth's speak sentence BXML verb

@copyright Bandwidth INC
"""

from lxml import etree

from .base_verb import AbstractBxmlVerb

import re

BRIDGE_TAG = "Bridge"

class Bridge(AbstractBxmlVerb):

    def __init__(self, call_id, bridge_complete_url=None, bridge_complete_method=None,
            bridge_target_complete_url=None, bridge_target_complete_method=None,
            username=None, password=None, tag=None, bridge_complete_fallback_url=None,
            bridge_complete_fallback_method=None, bridge_target_complete_fallback_url=None,
            bridge_target_complete_fallback_method=None, fallback_username=None,
            fallback_password=None):
        """
        Initializes the Bridge class with the following parameters

        :param str call_id: The call to bridge
        :param str bridge_complete_url: URL to send the bridge complete event to 
        :param str bridge_complete_method: HTTP method to send the bridge complete event
        :param str bridge_target_complete_url: URL to send the bridge target complete event to 
        :param str bridge_target_complete_method: HTTP method to send the bridge target complete event 
        :param str username: HTTP basic auth username for events
        :param str password: HTTP basic auth password for events
        :param str tag: Custom tag to include in callbacks 
        :param str bridge_complete_fallback_url: Fallback url for bridge complete events
        :param str bridge_complete_fallback_method: HTTP method for bridge complete fallback
        :param str bridge_target_complete_fallback_url: Fallback url for bridge target complete events
        :param str bridge_target_complete_fallback_method: HTTP method for bridge target complete fallback
        :param str fallback_username: Basic auth username for fallback events
        :param str fallback_password: Basic auth password for fallback events
        """
        self.call_id = call_id
        self.bridge_complete_url = bridge_complete_url
        self.bridge_complete_method = bridge_complete_method
        self.bridge_target_complete_url = bridge_target_complete_url
        self.bridge_target_complete_method = bridge_target_complete_method
        self.username = username
        self.password = password
        self.tag = tag
        self.bridge_complete_fallback_url = bridge_complete_fallback_url
        self.bridge_complete_fallback_method = bridge_complete_fallback_method
        self.bridge_target_complete_fallback_url = bridge_target_complete_fallback_url
        self.bridge_target_complete_fallback_method = bridge_target_complete_fallback_method
        self.fallback_username = fallback_username
        self.fallback_password = fallback_password

    def to_bxml(self):
        root = etree.Element(BRIDGE_TAG)
        root.text = self.call_id
        if self.bridge_complete_url is not None:
            root.set("bridgeCompleteUrl", self.bridge_complete_url)
        if self.bridge_complete_method is not None:
            root.set("bridgeCompleteMethod", self.bridge_complete_method)
        if self.bridge_target_complete_url is not None:
            root.set("bridgeTargetCompleteUrl", self.bridge_target_complete_url)
        if self.bridge_target_complete_method is not None:
            root.set("bridgeTargetCompleteMethod", self.bridge_target_complete_method)
        if self.username is not None:
            root.set("username", self.username)
        if self.password is not None:
            root.set("password", self.password)
        if self.tag is not None:
            root.set("tag", self.tag)
        if self.bridge_complete_fallback_url is not None:
            root.set("bridgeCompleteFallbackUrl", self.bridge_complete_fallback_url)
        if self.bridge_complete_fallback_method is not None:
            root.set("bridgeCompleteFallbackMethod", self.bridge_complete_fallback_method)
        if self.bridge_target_complete_fallback_url is not None:
            root.set("bridgeTargetCompleteFallbackUrl", self.bridge_target_complete_fallback_url)
        if self.bridge_target_complete_fallback_method is not None:
            root.set("bridgeTargetCompleteFallbackMethod", self.bridge_target_complete_fallback_method)
        if self.fallback_username is not None:
            root.set("fallbackUsername", self.fallback_username)
        if self.fallback_password is not None:
            root.set("fallbackPassword", self.fallback_password)
        return etree.tostring(root).decode()
