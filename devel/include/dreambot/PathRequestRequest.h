// Generated by gencpp from file dreambot/PathRequestRequest.msg
// DO NOT EDIT!


#ifndef DREAMBOT_MESSAGE_PATHREQUESTREQUEST_H
#define DREAMBOT_MESSAGE_PATHREQUESTREQUEST_H


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
struct PathRequestRequest_
{
  typedef PathRequestRequest_<ContainerAllocator> Type;

  PathRequestRequest_()
    : path_name()  {
    }
  PathRequestRequest_(const ContainerAllocator& _alloc)
    : path_name(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _path_name_type;
  _path_name_type path_name;





  typedef boost::shared_ptr< ::dreambot::PathRequestRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::dreambot::PathRequestRequest_<ContainerAllocator> const> ConstPtr;

}; // struct PathRequestRequest_

typedef ::dreambot::PathRequestRequest_<std::allocator<void> > PathRequestRequest;

typedef boost::shared_ptr< ::dreambot::PathRequestRequest > PathRequestRequestPtr;
typedef boost::shared_ptr< ::dreambot::PathRequestRequest const> PathRequestRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::dreambot::PathRequestRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::dreambot::PathRequestRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::dreambot::PathRequestRequest_<ContainerAllocator1> & lhs, const ::dreambot::PathRequestRequest_<ContainerAllocator2> & rhs)
{
  return lhs.path_name == rhs.path_name;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::dreambot::PathRequestRequest_<ContainerAllocator1> & lhs, const ::dreambot::PathRequestRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace dreambot

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::dreambot::PathRequestRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::dreambot::PathRequestRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::dreambot::PathRequestRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::dreambot::PathRequestRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dreambot::PathRequestRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dreambot::PathRequestRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::dreambot::PathRequestRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "3572e731ca915997319cdf3e8b7f260b";
  }

  static const char* value(const ::dreambot::PathRequestRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x3572e731ca915997ULL;
  static const uint64_t static_value2 = 0x319cdf3e8b7f260bULL;
};

template<class ContainerAllocator>
struct DataType< ::dreambot::PathRequestRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "dreambot/PathRequestRequest";
  }

  static const char* value(const ::dreambot::PathRequestRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::dreambot::PathRequestRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string path_name\n"
;
  }

  static const char* value(const ::dreambot::PathRequestRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::dreambot::PathRequestRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.path_name);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct PathRequestRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::dreambot::PathRequestRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::dreambot::PathRequestRequest_<ContainerAllocator>& v)
  {
    s << indent << "path_name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.path_name);
  }
};

} // namespace message_operations
} // namespace ros

#endif // DREAMBOT_MESSAGE_PATHREQUESTREQUEST_H