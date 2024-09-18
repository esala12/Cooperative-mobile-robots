// Auto-generated. Do not edit!

// (in-package dreambot.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class ControlFeedback {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.distance_to_goal = null;
    }
    else {
      if (initObj.hasOwnProperty('distance_to_goal')) {
        this.distance_to_goal = initObj.distance_to_goal
      }
      else {
        this.distance_to_goal = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ControlFeedback
    // Serialize message field [distance_to_goal]
    bufferOffset = _serializer.float64(obj.distance_to_goal, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ControlFeedback
    let len;
    let data = new ControlFeedback(null);
    // Deserialize message field [distance_to_goal]
    data.distance_to_goal = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'dreambot/ControlFeedback';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '6ad47d3db7202cba81252eaa6fcd95a5';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
    float64 distance_to_goal  # Feedback - current distance to the goal
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ControlFeedback(null);
    if (msg.distance_to_goal !== undefined) {
      resolved.distance_to_goal = msg.distance_to_goal;
    }
    else {
      resolved.distance_to_goal = 0.0
    }

    return resolved;
    }
};

module.exports = ControlFeedback;
