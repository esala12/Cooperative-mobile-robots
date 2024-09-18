// Generated by gencpp from file dreambot/PathRequestResponse.msg
// DO NOT EDIT!


#ifndef DREAMBOT_MESSAGE_PATHREQUESTRESPONSE_H
#define DREAMBOT_MESSAGE_PATHREQUESTRESPONSE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace dreambot
{
template <class ContainerAllocator>
struct PathRequestResponse_
{
  typedef PathRequestResponse_<ContainerAllocator> Type;

  PathRequestResponse_()
    : success(false)
    , message()  {
    }
  PathRequestResponse_(const ContainerAllocator& _alloc)
    : success(false)
    , message(_alloc)  {
  (void)_alloc;
    }



   typedef uint8_t _success_type;
  _success_type success;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _message_type;
  _message_type message;





  typedef boost::shared_ptr< ::dreambot::PathRequestResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::dreambot::PathRequestResponse_<ContainerAllocator> const> ConstPtr;

}; // struct PathRequestResponse_

typedef ::dreambot::PathRequestResponse_<std::allocator<void> > PathRequestResponse;

typedef boost::shared_ptr< ::dreambot::PathRequestResponse > PathRequestResponsePtr;
typedef boost::shared_ptr< ::dreambot::PathRequestResponse const> PathRequestResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::dreambot::PathRequestResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::dreambot::PathRequestResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::dreambot::PathRequestResponse_<ContainerAllocator1> & lhs, const ::dreambot::PathRequestResponse_<ContainerAllocator2> & rhs)
{
  return lhs.success == rhs.success &&
    lhs.message == rhs.message;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::dreambot::PathRequestResponse_<ContainerAllocator1> & lhs, const ::dreambot::PathRequestResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace dreambot

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::dreambot::PathRequestResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::dreambot::PathRequestResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::dreambot::PathRequestResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::dreambot::PathRequestResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dreambot::PathRequestResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dreambot::PathRequestResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::dreambot::PathRequestResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "937c9679a518e3a18d831e57125ea522";
  }

  static const char* value(const ::dreambot::PathRequestResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x937c9679a518e3a1ULL;
  static const uint64_t static_value2 = 0x8d831e57125ea522ULL;
};

template<class ContainerAllocator>
struct DataType< ::dreambot::PathRequestResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "dreambot/PathRequestResponse";
  }

  static const char* value(const ::dreambot::PathRequestResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::dreambot::PathRequestResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool success\n"
"string message\n"
"\n"
;
  }

  static const char* value(const ::dreambot::PathRequestResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::dreambot::PathRequestResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.success);
      stream.next(m.message);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct PathRequestResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::dreambot::PathRequestResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::dreambot::PathRequestResponse_<ContainerAllocator>& v)
  {
    s << indent << "success: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.success);
    s << indent << "message: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.message);
  }
};

} // namespace message_operations
} // namespace ros

#endif // DREAMBOT_MESSAGE_PATHREQUESTRESPONSE_H
