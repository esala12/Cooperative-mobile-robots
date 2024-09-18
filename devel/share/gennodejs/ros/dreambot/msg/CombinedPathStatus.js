// Auto-generated. Do not edit!

// (in-package dreambot.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let PathArray = require('./PathArray.js');

//-----------------------------------------------------------

class CombinedPathStatus {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.path = null;
      this.node_active = null;
      this.path_published = null;
    }
    else {
      if (initObj.hasOwnProperty('path')) {
        this.path = initObj.path
      }
      else {
        this.path = new PathArray();
      }
      if (initObj.hasOwnProperty('node_active')) {
        this.node_active = initObj.node_active
      }
      else {
        this.node_active = false;
      }
      if (initObj.hasOwnProperty('path_published')) {
        this.path_published = initObj.path_published
      }
      else {
        this.path_published = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type CombinedPathStatus
    // Serialize message field [path]
    bufferOffset = PathArray.serialize(obj.path, buffer, bufferOffset);
    // Serialize message field [node_active]
    bufferOffset = _serializer.bool(obj.node_active, buffer, bufferOffset);
    // Serialize message field [path_published]
    bufferOffset = _serializer.bool(obj.path_published, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type CombinedPathStatus
    let len;
    let data = new CombinedPathStatus(null);
    // Deserialize message field [path]
    data.path = PathArray.deserialize(buffer, bufferOffset);
    // Deserialize message field [node_active]
    data.node_active = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [path_published]
    data.path_published = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += PathArray.getMessageSize(object.path);
    return length + 2;
  }

  static datatype() {
    // Returns string type for a message object
    return 'dreambot/CombinedPathStatus';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5fe88b32f7d29dd3ec2430f387f8a6ea';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    dreambot/PathArray path
    bool node_active
    bool path_published
    
    ================================================================================
    MSG: dreambot/PathArray
    float64[] x
    float64[] y
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new CombinedPathStatus(null);
    if (msg.path !== undefined) {
      resolved.path = PathArray.Resolve(msg.path)
    }
    else {
      resolved.path = new PathArray()
    }

    if (msg.node_active !== undefined) {
      resolved.node_active = msg.node_active;
    }
    else {
      resolved.node_active = false
    }

    if (msg.path_published !== undefined) {
      resolved.path_published = msg.path_published;
    }
    else {
      resolved.path_published = false
    }

    return resolved;
    }
};

module.exports = CombinedPathStatus;
