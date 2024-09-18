// Generated by gencpp from file dreambot/PathRequest.msg
// DO NOT EDIT!


#ifndef DREAMBOT_MESSAGE_PATHREQUEST_H
#define DREAMBOT_MESSAGE_PATHREQUEST_H

#include <ros/service_traits.h>


#include <dreambot/PathRequestRequest.h>
#include <dreambot/PathRequestResponse.h>


namespace dreambot
{

struct PathRequest
{

typedef PathRequestRequest Request;
typedef PathRequestResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct PathRequest
} // namespace dreambot


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::dreambot::PathRequest > {
  static const char* value()
  {
    return "6ecd13868fafba67899de9f7428020dc";
  }

  static const char* value(const ::dreambot::PathRequest&) { return value(); }
};

template<>
struct DataType< ::dreambot::PathRequest > {
  static const char* value()
  {
    return "dreambot/PathRequest";
  }

  static const char* value(const ::dreambot::PathRequest&) { return value(); }
};


// service_traits::MD5Sum< ::dreambot::PathRequestRequest> should match
// service_traits::MD5Sum< ::dreambot::PathRequest >
template<>
struct MD5Sum< ::dreambot::PathRequestRequest>
{
  static const char* value()
  {
    return MD5Sum< ::dreambot::PathRequest >::value();
  }
  static const char* value(const ::dreambot::PathRequestRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::dreambot::PathRequestRequest> should match
// service_traits::DataType< ::dreambot::PathRequest >
template<>
struct DataType< ::dreambot::PathRequestRequest>
{
  static const char* value()
  {
    return DataType< ::dreambot::PathRequest >::value();
  }
  static const char* value(const ::dreambot::PathRequestRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::dreambot::PathRequestResponse> should match
// service_traits::MD5Sum< ::dreambot::PathRequest >
template<>
struct MD5Sum< ::dreambot::PathRequestResponse>
{
  static const char* value()
  {
    return MD5Sum< ::dreambot::PathRequest >::value();
  }
  static const char* value(const ::dreambot::PathRequestResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::dreambot::PathRequestResponse> should match
// service_traits::DataType< ::dreambot::PathRequest >
template<>
struct DataType< ::dreambot::PathRequestResponse>
{
  static const char* value()
  {
    return DataType< ::dreambot::PathRequest >::value();
  }
  static const char* value(const ::dreambot::PathRequestResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // DREAMBOT_MESSAGE_PATHREQUEST_H
