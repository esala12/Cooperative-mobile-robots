// Generated by gencpp from file dreambot/CombinedPathStatus.msg
// DO NOT EDIT!


#ifndef DREAMBOT_MESSAGE_COMBINEDPATHSTATUS_H
#define DREAMBOT_MESSAGE_COMBINEDPATHSTATUS_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <dreambot/PathArray.h>

namespace dreambot
{
template <class ContainerAllocator>
struct CombinedPathStatus_
{
  typedef CombinedPathStatus_<ContainerAllocator> Type;

  CombinedPathStatus_()
    : path()
    , node_active(false)
    , path_published(false)  {
    }
  CombinedPathStatus_(const ContainerAllocator& _alloc)
    : path(_alloc)
    , node_active(false)
    , path_published(false)  {
  (void)_alloc;
    }



   typedef  ::dreambot::PathArray_<ContainerAllocator>  _path_type;
  _path_type path;

   typedef uint8_t _node_active_type;
  _node_active_type node_active;

   typedef uint8_t _path_published_type;
  _path_published_type path_published;





  typedef boost::shared_ptr< ::dreambot::CombinedPathStatus_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::dreambot::CombinedPathStatus_<ContainerAllocator> const> ConstPtr;

}; // struct CombinedPathStatus_

typedef ::dreambot::CombinedPathStatus_<std::allocator<void> > CombinedPathStatus;

typedef boost::shared_ptr< ::dreambot::CombinedPathStatus > CombinedPathStatusPtr;
typedef boost::shared_ptr< ::dreambot::CombinedPathStatus const> CombinedPathStatusConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::dreambot::CombinedPathStatus_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::dreambot::CombinedPathStatus_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::dreambot::CombinedPathStatus_<ContainerAllocator1> & lhs, const ::dreambot::CombinedPathStatus_<ContainerAllocator2> & rhs)
{
  return lhs.path == rhs.path &&
    lhs.node_active == rhs.node_active &&
    lhs.path_published == rhs.path_published;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::dreambot::CombinedPathStatus_<ContainerAllocator1> & lhs, const ::dreambot::CombinedPathStatus_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace dreambot

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::dreambot::CombinedPathStatus_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::dreambot::CombinedPathStatus_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::dreambot::CombinedPathStatus_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::dreambot::CombinedPathStatus_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dreambot::CombinedPathStatus_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dreambot::CombinedPathStatus_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::dreambot::CombinedPathStatus_<ContainerAllocator> >
{
  static const char* value()
  {
    return "5fe88b32f7d29dd3ec2430f387f8a6ea";
  }

  static const char* value(const ::dreambot::CombinedPathStatus_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x5fe88b32f7d29dd3ULL;
  static const uint64_t static_value2 = 0xec2430f387f8a6eaULL;
};

template<class ContainerAllocator>
struct DataType< ::dreambot::CombinedPathStatus_<ContainerAllocator> >
{
  static const char* value()
  {
    return "dreambot/CombinedPathStatus";
  }

  static const char* value(const ::dreambot::CombinedPathStatus_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::dreambot::CombinedPathStatus_<ContainerAllocator> >
{
  static const char* value()
  {
    return "dreambot/PathArray path\n"
"bool node_active\n"
"bool path_published\n"
"\n"
"================================================================================\n"
"MSG: dreambot/PathArray\n"
"float64[] x\n"
"float64[] y\n"
;
  }

  static const char* value(const ::dreambot::CombinedPathStatus_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::dreambot::CombinedPathStatus_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.path);
      stream.next(m.node_active);
      stream.next(m.path_published);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct CombinedPathStatus_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::dreambot::CombinedPathStatus_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::dreambot::CombinedPathStatus_<ContainerAllocator>& v)
  {
    s << indent << "path: ";
    s << std::endl;
    Printer< ::dreambot::PathArray_<ContainerAllocator> >::stream(s, indent + "  ", v.path);
    s << indent << "node_active: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.node_active);
    s << indent << "path_published: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.path_published);
  }
};

} // namespace message_operations
} // namespace ros

#endif // DREAMBOT_MESSAGE_COMBINEDPATHSTATUS_H
